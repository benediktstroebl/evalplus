
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
    import pandas as pd
    df = pd.read_csv('planets.csv')
    df = df.drop(columns=['planet'])

    def find_row(planet):
        if planet == 'Mercury':
            return 0
        elif planet == 'Venus':
            return 1
        elif planet == 'Earth':
            return 2
        elif planet == 'Mars':
            return 3
        elif planet == 'Jupiter':
            return 4
        elif planet == 'Saturn':
            return 5
        elif planet == 'Uranus':
            return 6
        elif planet == 'Neptune':
            return 7
        else:
            return None

    planet1_row = find_row(planet1)
    planet2_row = find_row(planet2)

    if planet1_row == None or planet2_row == None:
        return ()

    df = df.loc[(df['row']>planet1_row) & (df['row']<planet2_row)]
    df = df.sort_values(by='row')
    df = df.drop(columns=['row'])
    return tuple(df.planet.tolist())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
