
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

    planets = {
        "Mercury": ["Venus", "Earth", "Mars"],
        "Venus": ["Earth", "Mars", "Jupiter"],
        "Earth": ["Mars", "Jupiter", "Saturn"],
        "Mars": ["Jupiter", "Saturn", "Uranus"],
        "Jupiter": ["Saturn", "Uranus", "Neptune"],
        "Saturn": ["Uranus", "Neptune"],
        "Uranus": ["Neptune"],
        "Neptune": []
    }
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    visited = set()
    to_visit = [(planet1, 0)]
    while to_visit:
        current_planet, count = to_visit.pop(0)
        visited.add(current_planet)
        for neighbor in planets[current_planet]:
            if neighbor not in visited:
                if neighbor == planet2:
                    return (planet2,) + tuple(sorted(planets[planet2], key
