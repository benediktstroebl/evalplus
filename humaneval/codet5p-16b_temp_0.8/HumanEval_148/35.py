
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

    
    planets = { "Mercury": 0.387, "Venus": 0.723, "Earth": 1, "Mars": 1.524, "Jupiter": 11.86, "Saturn": 29.447, "Uranus": 84.0168, "Neptune": 164.79 }
    
    planet1_dist = planets[planet1]
    planet2_dist = planets[planet2]
    
    midpoint = (planet1_dist + planet2_dist) / 2
    
    planet_names = []
    
    for planet in planets:
        planet_dist = planets[planet]
        if planet_dist < midpoint:
            planet_names.append(planet)
    
    return tuple(sorted(planet_names))
