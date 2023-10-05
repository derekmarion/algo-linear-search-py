def linear_search(searchTerm, arr):
    for element in arr: #iterate through array and compare to search term
        if element == searchTerm:
            return arr.index(element)
    return None

def linear_search_global(searchTerm, arr):
    output = []
    i = 0
    for element in arr:
        if element == searchTerm:
            output.append(i)
        i += 1
    return output