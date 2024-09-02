
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_len = len(lst)

    if lst_len <= 1:
        return lst

    initial_index = 0
    last_index = lst_len - 1
    while initial_index < last_index:
        if lst[initial_index] % 2 == 0 and lst[last_index] % 2 == 0:
            lst[initial_index] += lst[last_index]
            lst[last_index] = 0
            initial_index += 1
            last_index -= 1
        elif lst[initial_index] % 2 == 0:
            lst[initial_index] += lst[last_index]
            lst[last_index] = 0
            initial_index += 1
            last_index -= 1
        elif lst[last_index] % 2 == 0:
            lst[last_index] += lst[initial_index]
            lst[initial_index] = 0
            last_index -= 1
            initial_index += 1
        else:
            break

    return lst

