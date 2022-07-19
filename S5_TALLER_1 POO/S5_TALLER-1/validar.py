import re


class Valid:

    def Valid_ced():
        pass

    def Valid_correo():
        pass


    def Valid_ced(ced):
        ced2 = ced.isdigit()
        if ced2 == True:
            return True
        else:
            return False

    def Valid_correo(correo):
        if re.match('^[(a-z0-9\_\-\.)]+@[gmail,hotmail,outlook,unemi]+\.[(a-z)]',correo.lower()):
            return True
            
        else:
            return False

    def Valid_clave(clave):
        key2 = clave.isdigit()
        
        if key2 == True:
            return True
        else:
            return False