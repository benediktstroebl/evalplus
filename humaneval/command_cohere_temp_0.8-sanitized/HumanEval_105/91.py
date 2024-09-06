import unittest
def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(NUMBER_TO_NAME[num])
    return result if result else []
NUMBER_TO_NAME = {1: "One", 2: "Two", 3: "Three", 4: "Four", 
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}