
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
    get_planet_names = {
                      'Mercury':('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                      'Venus':('Mercury', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                      'Earth':('Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                      'Mars':('Mercury', 'Venus', 'Earth', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'),
                      'Jupiter':('Mercury', 'Venus', 'Earth', 'Mars', 'Saturn', 'Uranus', 'Neptune'),
                      'Saturn':('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Uranus', 'Neptune'),
                      'Uranus':('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune'),
                      'Neptune':('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus'),
                      }
    if planet1 in get_planet_names and planet2 in get_planet_names:
        result = [planet for planet in get_planet_names[planet1] if planet in get_planet_names[planet2]]
        if result == []:
            return ()
        else:
            return tuple(result[::-1])
    else:
        return ()