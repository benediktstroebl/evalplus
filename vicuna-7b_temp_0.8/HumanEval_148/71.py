
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
    if not is_planet_name(planet1) or not is_planet_name(planet2):
        return ()
    planets = [planet1, planet2]
    for i in range(1, len(planets)):
        current_planet = planets[i]
        if is_planet_name(current_planet):
            planets.remove(current_planet)
        if current_planet > planets[i-1]:
            break
        if planets[i-1] < planets[i]:
            break
        elif planets[i-1] == planets[i]:
            break
    else:
        return tuple(planets)
