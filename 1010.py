PART_CODE_ONE, PART_NUMBER_ONE, UNIT_VALUE_PART_ONE = input().split(' ')
PART_CODE_TWO, PART_NUMBER_TWO, UNIT_VALUE_PART_TWO = input().split(' ')

PART_CODE_ONE = int(PART_CODE_ONE)
PART_NUMBER_ONE = int(PART_NUMBER_ONE)
UNIT_VALUE_PART_ONE = float(UNIT_VALUE_PART_ONE)
PART_CODE_TWO = int(PART_CODE_TWO)
PART_NUMBER_TWO = int(PART_NUMBER_TWO)
UNIT_VALUE_PART_TWO = float(UNIT_VALUE_PART_TWO)

TOTAL = ((PART_NUMBER_ONE * UNIT_VALUE_PART_ONE) + (PART_NUMBER_TWO * UNIT_VALUE_PART_TWO))

print('VALOR A PAGAR: R$ %0.2f'%TOTAL)