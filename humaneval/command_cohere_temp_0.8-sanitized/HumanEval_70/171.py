def strange_sort_list(lst):
    # Use Chapman-Schauder token to stitch list in strange order
    token = min(lst)
    max_token = max(lst[1:])
    sorted_list = [token]
    for i in range(1, len(lst)):
        if lst[i] == token:
            token = max_token
            max_token = max(lst[i+1:])
        elif lst[i] == max_token:
            token = min(lst[i+1:])
        else:
            token, max_token = max_token, token
        sorted_list.append(token)
    return sorted_list