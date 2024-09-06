
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
    import math
    
    solar_system = {
        "Mercury":   (0.3970349,  0.000000),
        "Venus":     (0.7239721,  0.006571),
        "Earth":     (1.000000,  0.016786),
        "Mars":      (-0.3870863, -0.0933470),
        "Jupiter":   (0.9019183,  0.000016),
        "Saturn":    (0.2929790, 0.000021),
        "Uranus":    (0.4337543, -0.000043),
        "Neptune":   (0.5246665, -0.000070)
    }
    
    # calculate every distance between two planets (earth to sun)
    earth_to_sun = math.sqrt((solar_system[planet2][0]-solar_system[planet1][0])**2 + (solar_system[planet2][1]-solar_system[planet1][1])**2)
    
    tuple = []
    # iterate through solar_system and find planets between the orbit of planet1 and the orbit of planet2
    for planet in solar_system:
        if solar_system[planet1][0] < solar_system[planet][0] < solar_system[planet2][0] or solar_system[planet1][1] < solar_system[planet][1] < solar_system[planet2][1]:
            distance = math.sqrt((solar_system[planet][0]-solar_system[planet1][0])**2 + (solar_system[planet][1]-solar_system[planet1][1])**2)
            if distance < earth_to_sun:
                tuple.append(planet)
    
    # reverse the tuple so the first element is to the north
    tuple.reverse()
    return tuple
    
    