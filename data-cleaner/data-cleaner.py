
import streamlit as st
import pandas as pd
from io import BytesIO
import openpyxl

# Set up the Streamlit page
st.set_page_config(page_title="🧹 File Converter & Cleaner", layout="wide")
st.title("🧹 File Converter & Cleaner")
st.write("📤 Upload Your Files to Convert (CSV or Excel)")

# Upload CSV or Excel files
files = st.file_uploader("📁 Upload CSV or Excel File", type=["csv", "xlsx"], accept_multiple_files=True)

#file = st.file_uploader("Upload a file", type=["csv", "xlsx"],accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1].lower()

        # Read the file depending on extension
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        # Display preview
        st.subheader(f"👀 Preview of {file.name}")
        st.dataframe(df.head())

        # Checkbox to fill missing values
        if st.checkbox(f"Fill Missing Values - {file.name}"):
            # Fill missing numeric values
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("✅ Missing values filled successfully!")
            st.dataframe(df.head())

        # Multiselect to choose which columns to keep
        selected_columns = st.multiselect(f"Select Columns to Keep - {file.name}", df.columns, default=list(df.columns))
        df = df[selected_columns]
        st.write("🔍 Filtered Data Preview:")
        st.dataframe(df.head())

        format_choice = st.radio(f"📤Select to Convert File {file.name} to format:", ["CSV", "Excel"], key=f"format_{file.name}")
        if st.button(f"⏬Download {file.name} as {format_choice}"):
             
             output = BytesIO()
             if format_choice == "csv":
                 df.to_csv(output, index=False)
                 mime ="text/csv"
                 new_name = file.name.replace(ext, "csv")

             else:
                 
                 df.to_excel(output, index=False)
                 mime = "application/vnd.openxmlformats-officedocuments.spreadsheetml.sheet"
                 new_name = file.name.replace(ext, "xlsx")
                 output.seek(0)
             st.download_button(label="⏬ Download File",data=output, file_name=new_name,mime=mime)
             st.success("Processing Completed Click ⏬  to download ")
             