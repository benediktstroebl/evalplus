
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
    if planet1 not in PLANETS or planet2 not in PLANETS:
        return ()
    if planet1 == planet2:
        return (planet1, )

    class Planet(object):
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name
    
    def dist(p1, p2):
        x1, y1 = points[p1]
        x2, y2 = points[p2]
        return abs(x1-x2) + abs(y1-y2)

    p1 = PLANETS[planet1]
    p2 = PLANETS[planet2]

    def dfs(path, visited, target):
        if visited.count(True) == len(PLANETS):
            return path
        if target not in visited:
            visited[target] = True
            for child in sorted(p1.children, key=lambda p: dist(p, target)):
                if not visited[child]:
                    visited[child] = True
                    path.append(child)
                    result = dfs(path[:], visited, target)
                    if result:
                        return result
                    path.pop()
                    visited[child] = False
        return []

    ret = []
    points = {p.name: p.point for p in PLANETS.values()}
    for p in PLANETS.values():
        visited = {p.name: False}
        visited[p.name] = True
        dfs([p.name], visited, target=p.name)
        if visited[p.name]:
            ret.append(p.name)
            
    return tuple(ret)
