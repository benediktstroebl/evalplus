def by_length(arr):
    unsort = sorted(arr)
    unsort.reverse()
    result = []
    for num in unsort:
        if 1 <= num <= 9: 
            result.append(str(num)[0] + "een")
    return result if result else []