
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
    # check if the planets are valid
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    
    # check if the planets are valid
    if not planet1 in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    
    if not planet2 in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    
    # get the orbit of the first planet
    orbit1 = get_orbit(planet1)
    
    # get the orbit of the second planet
    orbit2 = get_orbit(planet2)
    
    # check if the orbit of the second planet is beyond the orbit of the first planet
    if orbit2 < orbit1:
        return ()
    
    # check if the orbit of the first planet is beyond the orbit of the second planet
    if orbit1 < orbit2:
        return ()
    
    # get the orbit of the second planet and convert it to the AU
    orbit2_au = convert_to_au(orbit2)
    
    # get the orbit of the first planet and convert it to the AU
    orbit1_au = convert_to_au(orbit1)
    
    # check if the orbits are located between the orbit of the first planet and the orbit of the second planet
    if orbit1_au < orbit2_au < orbit2:
        return (orbit1, orbit2)
    else:
        return ()
