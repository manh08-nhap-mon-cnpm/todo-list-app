# todo-list-app

Một ứng dụng To-Do List đơn giản bằng Python.

\# Danh sách để lưu các công việc

tasks = \[]



def add\_task(task\_name):

&nbsp;   """Thêm một công việc mới vào danh sách."""

&nbsp;   tasks.append(task\_name)

&nbsp;   print(f"Đã thêm công việc: '{task\_name}'")



\# --- Điểm bắt đầu của chương trình ---

if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   print("Chào mừng đến với ứng dụng To-Do List!")

&nbsp;   add\_task("Học bài Git và GitHub")

&nbsp;   add\_task("Làm bài tập thực hành ở nhà")



