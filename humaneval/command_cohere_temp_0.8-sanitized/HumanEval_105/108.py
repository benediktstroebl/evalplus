def by_length(arr):
    unsort = [int(x) for x in arr if 1 <= int(x) <= 9]
    sorted_unsort = sorted(unsort)
    reverse_sorted = [x for x in sorted_sol(sorted_unsort)]
    
    digits = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return [digits[i] for i in reverse_sorted]
def sorted_sol(arr):
    temp = []
    for x in arr:
        temp.append(x)
    return temp