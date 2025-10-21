# todo-list-app

Một ứng dụng To-Do List đơn giản bằng Python.

# Danh sách để lưu các công việc (mỗi công việc là 1 dictionary)
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """Liệt kê tất cả các công việc hiện có."""
    if not tasks:
        print("Chưa có công việc nào trong danh sách.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['name']}")

def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã đánh dấu hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số công việc không hợp lệ!")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    complete_task(0)  # đánh dấu công việc đầu tiên là hoàn thành
    list_tasks()
