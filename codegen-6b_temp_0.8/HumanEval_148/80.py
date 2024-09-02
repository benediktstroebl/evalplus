
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
    
    # first,find the index of the planet in the list by name
    planet1_index = 0
    planet2_index = 0

    for planet in planets:
        if planet == planet1:
            planet1_index = planets.index(planet)
        elif planet == planet2:
            planet2_index = planets.index(planet)

    #shorter-longest list
    if planet2_index > planet1_index:
        temp = planet1_index
        planet2_index = planet2_index
        planet1_index = temp
    
    #start from the beginning of the list
    planet1_index = planets.index(planet1) + 1

    #and end at the end of the list
    planet1_index = planets.index(planet2) -1

    #then list all the planets in between
    planet_list = planets[planet1_index:planet2_index+1]
    return tuple(sorted(planet_list))
