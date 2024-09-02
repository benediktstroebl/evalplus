
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
    # create an empty list
    planets = []
    
    # check if planet1 and planet2 are valid planet names
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return []
    
    # check if the planets are in the right order
    if planet1 > planet2:
        planets = [(planet2, planet1)]
    else:
        planets = [(planet1, planet2)]
    
    # check if the planet is a valid planet
    if isinstance(planet1, str) and isinstance(planet2, str):
        planets = [(planet, name) for name, planet in planets]
    
    return tuple(sorted(planets, key=lambda x: abs(sun_distance(x[0], x[1]) - sun_distance(planet1, planet2))))
