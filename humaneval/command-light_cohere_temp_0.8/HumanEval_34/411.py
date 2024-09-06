Here's the solution:

def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

This code defines a function `unique` which takes a list `lst` as an argument. It uses a unique elements method to filter out duplicates from the list, and then it creates a new list with the unique elements, which are then returned.