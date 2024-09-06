def by_length(arr):
    structured = [x for x in arr if 1 <= x <= 9]
    sorted_structured = sorted(structured)
    reversed_structured = sorted_structured[::-1]
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [names[i] for i in reversed_structured]
arr = [2, 1, 1, 4, 5, 8, 2, 3]