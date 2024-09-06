def by_length(arr):
    sorted_arr = sorted(arr)
    filtered_digits = [num for num in sorted_arr if 1 <= num <= 9]
    reversed_digits = filtered_digits[::-1]
    names = []
    for num in reversed_digits:
        names.append(num_to_word(num))
    return names if names else []
def num_to_word(num):
    words = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    return words.get(num, "")