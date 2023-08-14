def linear_search(value_to_find, array_to_search_through):
    # your code here
    for idx in range(len(array_to_search_through)):
        if array_to_search_through[idx] == value_to_find:
            return idx
    return None

def linear_search_global(value_to_find, array_to_search_through):
    # your code here
    answer = []
    for idx in range(len(array_to_search_through)):
        if array_to_search_through[idx] == value_to_find:
            answer.append(idx)
    return answer if answer else None