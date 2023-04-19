import streamlit as st


def app():
    st.title("Name : Priyanshu Priyadarshi")
    st.title("Roll number : 21f1000765")

    st.title("Find the Maximum Number")

    # Ask the user to input three numbers
    num1 = st.number_input("Enter the first number", value=0, step=1)
    num2 = st.number_input("Enter the second number", value=0, step=1)
    num3 = st.number_input("Enter the third number", value=0, step=1)

    # Add a button to find the maximum number
    if st.button("Find Maximum"):
        # Find the maximum of the three numbers
        max_num = max(num1, num2, num3)

        # Display the maximum number on the screen
        st.write("The maximum number is:", max_num)


if __name__ == "__main__":
    app()
