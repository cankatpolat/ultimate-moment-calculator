
try:

    import math
    concrete = input("Concrete is C30 Concrete (Y/N)? :")
    steel = input("Steel is S420 Steel (Y/N)? :")

    if concrete == "Y" and steel == "Y":
        areaSteel = float(input("Enter the area of steel (Ast) :"))

    else:
        print("Concrete must be C30 and Steel must be S420")


except ValueError:
    print("Answers must be only Y and N!")
