def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    named_arr = [name_digit_map[int(i)] for i in sorted_arr if 1 <= int(i) <= 9]
    return named_arr
digit_word_map = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}
name_digit_map = {v: k for k, v in digit_word_map.items()}