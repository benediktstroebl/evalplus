
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

    from ast import literal_eval as make_tuple
    from collections import deque
    orbit_tree = {}
    for i in open('data.txt').readlines():
        parent, child = i.split(")")
        orbit_tree[child] = parent
    q = deque()
    q.append(planet1)
    q.append(orbit_tree[planet1])
    orbit_tree[planet1] = tuple()
    orbit_tree[planet2] = tuple()
    while True:
        if q[0] == planet2:
            return tuple(orbit_tree.keys())
        if q[0] == orbit_tree[planet2]:
            return tuple(orbit_tree.keys())
        p = q.popleft()
        for i in orbit_tree.keys():
            if i == p:
                q.append(i)
        if p in orbit_tree.keys():
            q.append(orbit_tree[p])
            orbit_tree[p] = tuple()
        else:
            q.append(p)
            orbit_tree[
