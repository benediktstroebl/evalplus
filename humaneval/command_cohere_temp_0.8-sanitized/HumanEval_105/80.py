def by_length(arr):
    unsort = []
    for num in arr:
        if 1 <= num <= 9:
            unsort.append(num)
    unsort.sort()
    reverse = unsort[::-1]
    result = []
    for num in reverse:
        result.append(NUM_TO_NAME[num])
    return result if result else []
NUM_TO_NAME = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9}