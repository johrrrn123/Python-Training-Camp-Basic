def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 对于"add"、"remove"、"update"操作，返回更新后的字典
    - 对于"get"操作，返回对应的成绩值
    """
    if operation == "add":
        # 添加操作需要两个参数：姓名和成绩
        if len(args) != 2:
            raise ValueError("Add operation requires name and score")
        name, score = args
        students_dict[name] = score
        return students_dict
    
    elif operation == "remove":
        # 删除操作需要一个参数：姓名
        if len(args) != 1:
            raise ValueError("Remove operation requires name")
        name = args[0]
        if name not in students_dict:
            raise KeyError(f"{name} not found in dictionary")
        del students_dict[name]
        return students_dict
    
    elif operation == "update":
        # 更新操作需要两个参数：姓名和新成绩
        if len(args) != 2:
            raise ValueError("Update operation requires name and new score")
        name, new_score = args
        if name not in students_dict:
            raise KeyError(f"{name} not found in dictionary")
        students_dict[name] = new_score
        return students_dict
    
    elif operation == "get":
        # 查询操作需要一个参数：姓名
        if len(args) != 1:
            raise ValueError("Get operation requires name")
        name = args[0]
        if name not in students_dict:
            raise KeyError(f"{name} not found in dictionary")
        return students_dict[name]
    
    else:
        raise ValueError("Invalid operation. Use 'add', 'remove', 'update' or 'get'")