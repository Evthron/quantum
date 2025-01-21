import numpy as np

def norm(quantum_state):
    '''
    >>> q_state = np.array([1+2j, 3+4j])
    >>> norm(q_state)
    np.complex128(5.477225575051661+0j)
    '''
    return np.sqrt(scalar_product(quantum_state, quantum_state))

def outcome_probability(outcome_state, current_state):
    ''' born rule'''
    return modular_square(scalar_product(outcome_state, current_state))

def scalar_product(q_state_1, q_state_2):
    '''
    >>> q_state = np.array([1+1j, 1+1j])
    >>> scalar_product(q_state, q_state)
    np.complex128(4+0j)
    >>> q_state_1 = np.array([1+2j, 2+2j])
    >>> q_state_2 = np.array([1+3j, 1+2j])
    >>> scalar_product(q_state_1, q_state_2)
    np.complex128(13+3j)
    >>> modular_square(q_state_1[0]) + modular_square(q_state_1[1]) == scalar_product(q_state_1, q_state_1)
    np.True_
    '''
    return np.conj(q_state_1[0]) * q_state_2[0] + np.conj(q_state_1[1]) * q_state_2[1]

def is_orthonormal(quantum_state_1, quantum_state_2):
    '''
    >>> phi = np.array([1, 0])
    >>> psi = np.array([0, 0+1j])
    >>> is_orthonormal(phi, psi)
    np.True_
    '''
    return scalar_product(quantum_state_1, quantum_state_2) == 0

def kronecker_delta(m, n):
    return 1 if m == n else 0

def is_orthonormal_basis(quantum_states):
    '''
    >>> phi = np.array([1, 0])
    >>> psi = np.array([0, 0+1j])
    >>> q_states = [phi, psi]
    >>> is_orthonormal_basis(q_states)
    True
    '''
    for m in range(len(quantum_states)):
        if norm(quantum_states[m]) != 1:
            return False
        for n in range(m, len(quantum_states)):
            if scalar_product(quantum_states[m], quantum_states[n]) != kronecker_delta(m, n):
                return False
    return True


def convert_dirac_notation(quantum_state):
    #if not is_valid_quantum_state(quantum_state):
    #    return "not valid quantum state"
    zero_part = quantum_state[0]
    one_part = quantum_state[1]
    return f'{zero_part} |0> + {one_part} |1>'
    

def modular_square(complex_number):
    '''
    >>> phi = np.array([1, 0])
    >>> is_valid_quantum_state(phi)
    True
    >>> phi = np.array([0, 0+1j])
    >>> is_valid_quantum_state(phi)
    True
    '''
    '''
    >>> sqrt25 = np.sqrt(0.25)
    >>> phi = np.array([sqrt25+(sqrt25)*j, sqrt25+(sqrt25)*j])
    >>> is_valid_quantum_state(phi)
    True
    '''
    #print(np.real(complex_number) ** 2 + np.imag(complex_number) ** 2)
    return np.real(complex_number) ** 2 + np.imag(complex_number) ** 2

def is_valid_quantum_state(quantum_state):
    if len(quantum_state) != 2:
        return False
    elif modular_square(quantum_state[0]) + modular_square(quantum_state[1]) != 1:
        return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(convert_dirac_notation(np.array([1+2j, 3+4j])))
