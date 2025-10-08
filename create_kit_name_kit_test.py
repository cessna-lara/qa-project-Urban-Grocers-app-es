import sender_stand_request
import data

# Función para cambiar el valor del parámetro firstName en el cuerpo de la solicitud
def get_user_body(first_name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro Name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body

# Función de prueba positiva
def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(kit_body)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201


# Función de prueba negativa para los casos en los que la solicitud devuelve un error relacionado con caracteres
def negative_assert_code_400(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(kit_body)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400


    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "Los nombres solo pueden contener caracteres latinos, "\
                                         "los nombres deben tener al menos 1 caracteres y no más de 511 caracteres."

# Función de prueba negativa cuando el error es No se han aprobado todos los parámetros requeridos
def negative_assert_no_name(kit_body):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 1. Usuario o usuaria creada con éxito. El parámetro firstName contiene 1 caracter
def test_create_user_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body1)

# Prueba 2. Usuario o usuaria creada con éxito. El parámetro firstName contiene 511 caracteres
def test_create_user_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body2)


# Prueba 3. Error. El parámetro firstName contiene 0 carácter
def test_create_user_0_letter_in_name_get_error_response():
    negative_assert_code_400(data.kit_body3)


# Prueba 4. Error. El parámetro firstName contiene 512 caracteres
def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.kit_body4)

# Prueba 5. Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres especiales
def test_create_user_caracteres_letter_in_name_get_success_response():
    positive_assert(data.kit_body5)


# Prueba 6. Error. El parámetro firstName permite espacios
def test_create_user_has_special_symbol_in_name_get_error_response():
    positive_assert(data.kit_body6)


# Prueba 7. Error. El parámetro firstName contiene un string de dígitos
def test_create_user_has_number_in_name_get_error_response():
    positive_assert(data.kit_body7)

# Prueba 8. Error. Falta el parámetro firstName en la solicitud
def test_create_user_no_name_get_error_response():
   negative_assert_no_name(kit_body8)

# Prueba 9. Error. El tipo del parámetro firstName: número
def test_create_user_number_type_name_get_error_response():
    negative_assert_no_name(kit_body9)
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    kit_body = get_kit_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Comprobar el código de estado de la respuesta
    assert response.status_code == 400
