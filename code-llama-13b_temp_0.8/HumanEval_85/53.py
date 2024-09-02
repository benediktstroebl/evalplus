
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    def check(ind):
        return (ind % 2 == 1)

    def add_nums(lst):
        if lst == []:
            return 0

        val = lst[0]
        if val % 2 == 0:
            val += add_nums(lst[1:])
        else:
            val = add_nums(lst[1:])
        return val

    return add_nums(list(filter(check, lst)))

