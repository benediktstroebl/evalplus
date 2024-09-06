
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
    # check if planets are correct
    if not is_correct_planet(planet1) or not is_correct_planet(planet2):
        return ()
    
    # sort planets by proximity to the sun
    planets = sorted((is_correct_planet(planet), planet) for planet in (planet1, planet2))
    
    # check if planets are between the orbits of planet1 and planet2
    if is_correct_planet(planet1) and is_correct_planet(planet2):
        left_orbit = is_correct_planet(planet1)
        right_orbit = is_correct_planet(planet2)
        planets = sorted((planet, right_orbit - planet) for planet in planets if planet < right_orbit)
    else:
        planets = sorted((planet, 0) for planet in planets)
    
    # return planets
    return tuple(planets)
