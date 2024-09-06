
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
    # 2017-01-15: Please write your own code here
    
    # Determine the orbit of each planet
    planethelp()
    
    # Determine the closest planet to the Sun and the furthest
    min_distance, max_distance = 0, 0
    for i in range(1, 9):
        distance = _get_distance(planet1, planet2, i)
        if distance < min_distance:
            min_distance = distance
        elif distance > max_distance:
            max_distance = distance
    
    # Determine the orbit of each planet
    orbit_helper(min_distance, max_distance)
    
    # Return the sorted list of planets
    return sorted(planets, key=lambda x: (x.get_distance_to_the_sun(), x.name))
