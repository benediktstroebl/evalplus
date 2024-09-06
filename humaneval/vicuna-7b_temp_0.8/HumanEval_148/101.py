
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
    if not is_correct_planet_name(planet1) or not is_correct_planet_name(planet2):
        return ()
    else:
        planets = [planet1, planet2]
        for i in range(1, len(planets)):
            planet1_sun_distance = get_distance(planet1, sun)
            planet2_sun_distance = get_distance(planet2, sun)
            current_planet = planets[i]
            current_planet_sun_distance = get_distance(current_planet, sun)
            if planet1_sun_distance < current_planet_sun_distance < planet2_sun_distance:
                result = (planet1, planet2)
                break
            else:
                result = (planet2, planet1)
        return result
