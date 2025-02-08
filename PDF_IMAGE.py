import fitz  # PyMuPDF
from PIL import Image
import os

def save_pdf_images(pdf_path, output_folder):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打開PDF文件
    pdf_document = fitz.open(pdf_path)
    
    # 遍歷每一頁並提取圖片
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # 儲存圖片
            image_filename = f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
            image_filepath = os.path.join(output_folder, image_filename)
            with open(image_filepath, "wb") as image_file:
                image_file.write(image_bytes)
                
            print(f"Saved image {image_filename}")

# 使用示例
pdf_path = r"D:\SPV\藝人網紅\霖距離(霖霖).pdf" # PDF文件路徑
output_folder = "D:\SPV\藝人網紅\霖距離"  # 輸出資料夾
save_pdf_images(pdf_path, output_folder)
