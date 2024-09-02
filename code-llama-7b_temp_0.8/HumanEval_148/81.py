
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
    planet_names = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    planet_distances = (0.387, 0.723, 1.000, 1.524, 5.203, 9.540, 19.190, 30.060)
    planet_dict = dict(zip(planet_names, planet_distances))
    
    planet_names_sorted = sorted(planet_names, key=planet_dict.get)
    
    if planet1 in planet_names and planet2 in planet_names:
        try:
            planet1_idx = planet_names_sorted.index(planet1)
            planet2_idx = planet_names_sorted.index(planet2)
            return tuple(planet_names_sorted[planet1_idx+1: planet2_idx])
        except ValueError:
            return ()
    else:
        return ()
