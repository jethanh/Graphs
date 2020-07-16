
def earliest_ancestor(ancestors, starting_node):
    dictionary = {} 
    for ancestor in ancestors:
        if ancestor[1] in dictionary:
            dictionary[ancestor[1]].add(ancestor[0])
        else:
            dictionary[ancestor[1]] = {ancestor[0]}
        if ancestor[0] not in dictionary: 
            dictionary[ancestor[0]] = set()

    if len(dictionary[starting_node]) == 0: 
        return -1
    nxt = {starting_node}
    while len(nxt) > 0:
        current = nxt
        nxt = set()
        for node in current:
            nxt = nxt | dictionary[node]
    return min(current)