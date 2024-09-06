def strange_sort_list(lst):
    # Using integers to simulate sorting and filtering
    num = len(lst) - 1
    result = [x for x in lst if x == num or num == 0]
    while num > 0:
        num = (num - 1) // 2
        result.extend([x for x in lst if x != num and x != num + 1])
    return result