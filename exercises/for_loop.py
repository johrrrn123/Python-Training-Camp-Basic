def sum_numbers(n):
    """
    计算从1到n的所有整数之和
    
    参数:
    - n: 正整数
    
    返回:
    - 从1到n的所有整数之和
    """
    total = 0  # 初始化总和为0
    for i in range(1, n + 1):  # 遍历从1到n的所有整数
        total += i  # 将每个整数加到总和中
    return total