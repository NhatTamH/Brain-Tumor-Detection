import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ Tkinter
window = tk.Tk()

# Tạo đối tượng Label để hiển thị hình ảnh
image_label = tk.Label(window)
image_label.pack()

# Đường dẫn tới tập tin hình ảnh
image_path = "./out.jpg"

# Định nghĩa hàm để cập nhật hình ảnh trên Label
def update_image():
    # Đọc hình ảnh từ đường dẫn
    image = Image.open(image_path)

    # Chuyển đổi hình ảnh thành định dạng hiển thị trong Tkinter
    photo = ImageTk.PhotoImage(image)

    # Cập nhật hình ảnh trên Label
    image_label.configure(image=photo)
    image_label.image = photo  # Gán hình ảnh cho Label

# Gọi hàm cập nhật hình ảnh
update_image()

# Chạy giao diện Tkinter
window.mainloop()
