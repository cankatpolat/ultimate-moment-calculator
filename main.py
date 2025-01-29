try:
    concrete = input("Concrete is C30 Concrete (Y/N)? :")
    steel = input("Steel is S420 Steel (Y/N)? :")

    if concrete == "Y" and steel == "Y":
        areaSteel = float(input("Enter the area of steel (Ast) :"))

    else print()


except ValueError:
    print("Answers must be only Y and N!")
