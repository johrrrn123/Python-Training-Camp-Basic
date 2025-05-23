"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 创建列表的副本以避免修改原始列表
    new_list = students.copy()
    
    if operation == "add":
        # 添加操作：将新学生添加到列表末尾
        if len(args) > 0:
            new_list.append(args[0])
    elif operation == "remove":
        # 删除操作：从列表中移除指定的学生
        if len(args) > 0 and args[0] in new_list:
            new_list.remove(args[0])
    elif operation == "update":
        # 修改操作：将旧学生姓名更新为新姓名
        if len(args) > 1 and args[0] in new_list:
            index = new_list.index(args[0])
            new_list[index] = args[1]
    
    return new_list