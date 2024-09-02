
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
    if planet1 == 'Mercury':
        return tuple() if planet2 not in ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] else ('Venus',)
    if planet1 == 'Venus':
        return tuple() if planet2 not in ['Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] else ('Earth',)
    if planet1 == 'Earth':
        return tuple() if planet2 not in ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'] else ('Mars',)
    if planet1 == 'Mars':
        return tuple() if planet2 not in ['Jupiter', 'Saturn', 'Uranus', 'Neptune'] else ('Jupiter',)
    if planet1 == 'Jupiter':
        return tuple() if planet2 not in ['Saturn', 'Uranus', 'Neptune'] else ('Saturn',)
    if planet1 == 'Saturn':
        return tuple() if planet2 != 'Uranus' else ('Uranus',)
    if planet1 == 'Uranus':
        return tuple() if planet2 != 'Neptune' else ('Neptune',)
    if planet1 == 'Neptune':
        return tuple()
    return tuple()
