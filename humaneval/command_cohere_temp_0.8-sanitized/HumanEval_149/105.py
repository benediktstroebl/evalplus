def sorted_list_sum(lst):
    lst_length = len(lst)
    if lst_length % 2 == 0:
        return lst
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    new_lst.sort()
    return new_st
    # Add tests here
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]