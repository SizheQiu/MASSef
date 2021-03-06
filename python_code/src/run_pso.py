from pso_short_ver0091_rel_marta_test import run_pso
import sys


def _parse_function_parameters(parameter_file_in):
    """
    These parameters are imported from a text file constructed using the accompanying mathematica notebook.
    The parser expects two tab delimited elements in each line, which are placed in a dictionary object with
    the first elemnt being the key and the second element being the value.
        --All numerical values are imported as float values, reassign the values if another data type is needed.

    """

    """Import inputs by parsing from an argument file"""

    with open(parameter_file_in) as f_in:
        lines = f_in.readlines()

    parameter = dict()
    for line in lines[0:]:
        lineList = list()  # temp variable
        for elem in line.strip().split("\t"):
            try:
                lineList.append(float(elem))
            except:
                if (elem == 'True' or elem == 'False'):
                    """Assign Boolean Parameters"""
                    if (elem == 'True'):
                        lineList.append(True)
                    else:
                        lineList.append(False)
                else:
                    lineList.append(elem)
        parameter[lineList[0]] = lineList[1]
    """"""

    return parameter


if __name__ == '__main__':

    pso_parameter_file_in = '/home/mrama/Desktop/MD/kinetics/ENO/test/input/psoParameters_ENO_2017771251.txt'
    data_file_name = '/home/mrama/Desktop/MD/kinetics/ENO/test/input/ENO_dKd.dat'  # path to file with the data to be fit
    pso_summary_file_name = '/home/mrama/Desktop/MD/kinetics/ENO/test/output/raw/psoSummary.txt'
    pso_ultimate_result_file_name = '/home/mrama/Desktop/MD/kinetics/ENO/test/output/raw/psoResults.txt'

    pso_num_trials = 1

    # run pso
    pso_parameters = _parse_function_parameters(pso_parameter_file_in)
    print pso_parameters
    for i in range(pso_num_trials):
        run_pso(pso_parameters, data_file_name, pso_summary_file_name, pso_ultimate_result_file_name)
