
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
    try:
        if planet1.lower() =='mercury':
            planet1_num = 0
        elif planet1.lower() == 'jupiter':
            planet1_num = 4
        elif planet1.lower() =='venus':
            planet1_num = 1
        elif planet1.lower() =='mars':
            planet1_num = 2
        elif planet1.lower() =='saturn':
            planet1_num = 3
        elif planet1.lower() == 'uranus':
            planet1_num = 4
        elif planet1.lower() == 'neptune':
            planet1_num = 5
        elif planet1.lower() == 'earth':
            planet1_num = 1
        else:
            return ()
        if planet2.lower() =='mercury':
            planet2_num = 0
        elif planet2.lower() == 'jupiter':
            planet2_num = 4
        elif planet2.lower() =='venus':
            planet2_num = 1
        elif planet2.lower() =='mars':
            planet2_num = 2
        elif planet2.lower() =='saturn':
            planet2_num = 3
        elif planet2.lower() == 'uranus':
            planet2_num = 4
        elif planet2.lower() == 'neptune':
            planet2_num = 5
        elif planet2.lower() == 'earth':
            planet2_num = 1
        else:
            return ()
        return tuple(planet for planet in planets[planet1_num:planet2_num+1])
    except Exception:
        return ()
