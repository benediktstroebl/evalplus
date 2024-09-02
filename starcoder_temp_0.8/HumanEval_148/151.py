
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
    
    if planet1 in planets and planet2 in planets:
        if (planet1 == 'Mars' or planet1 == 'Saturn' or planet1 == 'Jupiter') and (planet2 == 'Mercury' or planet2 == 'Venus' or planet2 == 'Neptune'):
            return ()
        elif planet1 == planet2:
            return (planet1,)
        elif planet1 == 'Mercury' and planet2 == 'Venus':
            return ('Venus',)
        elif planet1 == 'Mercury' and planet2 == 'Mars':
            return ('Venus', 'Mars')
        elif planet1 == 'Mercury' and planet2 == 'Saturn':
            return ('Venus', 'Mars', 'Saturn')
        elif planet1 == 'Mercury' and planet2 == 'Jupiter':
            return ('Venus', 'Mars', 'Saturn', 'Jupiter')
        elif planet1 == 'Mercury' and planet2 == 'Neptune':
            return ('Venus', 'Mars', 'Saturn', 'Jupiter', 'Neptune')
        elif planet1 == 'Venus' and planet2 == 'Mars':
            return ('Mars',)
        elif planet1 == 'Venus' and planet2 == 'Saturn':
            return ('Mars', 'Saturn')
        elif planet1 == 'Venus' and planet2 == 'Jupiter':
            return ('Mars', 'Saturn', 'Jupiter')
        elif planet1 == 'Venus' and planet2 == 'Neptune':
            return ('Mars', 'Saturn', 'Jupiter', 'Neptune')
        elif planet1 == 'Earth' and planet2 == 'Mars':
            return ('Mars',)
        elif planet1 == 'Earth' and planet2 == 'Saturn':
            return ('Mars', 'Saturn')
        elif planet1 == 'Earth' and planet2 == 'Jupiter':
            return ('Mars', 'Saturn', 'Jupiter')
        elif planet1 == 'Earth' and planet2 == 'Neptune':
            return ('Mars', 'Saturn', 'Jupiter', 'Neptune')
        elif planet1 == 'Mars' and planet2 == 'Saturn':
            return ('Saturn',)
        elif planet1 == 'Mars' and planet2 ==
