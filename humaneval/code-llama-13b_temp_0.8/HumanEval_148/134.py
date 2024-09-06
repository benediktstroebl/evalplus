
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
    sun = 0
    mercury = 57.9
    venus = 108.2
    earth = 149.6
    mars = 227.9
    jupiter = 778.6
    saturn = 1433.5
    uranus = 2872.5
    neptune = 4495.1
    
    planet_name = ("Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune")
    planet_distance = (mercury, venus, earth, mars, jupiter, saturn, uranus, neptune)
    
    planet_dict = dict(zip(planet_name,planet_distance))
    
    if planet1 not in planet_name or planet2 not in planet_name:
        return ()
    else:
        planets = []
        for key in planet_dict.keys():
            if planet_dict[planet1] < planet_dict[key] < planet_dict[planet2]:
                planets.append(key)
        return tuple(planets)
    
