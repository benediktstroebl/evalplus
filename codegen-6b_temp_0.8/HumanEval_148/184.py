
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
    
    def search(planet_to_find, name, graph):
        if planet_to_find == name:
            return [name]
        elif planet_to_find in graph:
            search_list = graph[planet_to_find]
            for name in search_list:
                search_result = search(name, name, graph)
                if search_result:
                    return [planet_to_find] + search_result
            return []
        else:
            return []
    
    graph = {}
    
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        graph[planet] = []
        graph[planet].append(planet)
        graph[planet].append("Saturn")
        graph[planet].append("Uranus")
        graph[planet].append("Neptune")
        graph[planet].append("Earth")
    
    p1_orbit = search(planet1, planet1, graph)
    p2_orbit = search(planet2, planet2, graph)
    
    p1_orbit.sort(key=lambda x: (abs(len(p1_orbit) - len(p2_orbit)), len(p1_orbit)))
    
    return tuple(p1_orbit)
