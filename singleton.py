class Singleton(object):
    '''
    Share single instance of this class, initially created one
    '''
    instance = None

    def __new__(cls):
        if Singleton.instance is not None:
            return Singleton.instance
  
        Singleton.instance = object.__new__(cls)
        return Singleton.instance
