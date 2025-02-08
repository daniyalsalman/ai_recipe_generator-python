from helper_functions import get_llm_response

def recipe_generator( user_ingredient1,user_ingredient2,user_ingredient3,user_ingredient4,user_ingredient5) :
    # from some_llm_response import get_llm_response
    
    prompt=f"""use these ingredients given above {user_ingredient1},{user_ingredient2},{user_ingredient3},{user_ingredient4},{user_ingredient5} and generate 5 recipes"""
    recipes = get_llm_response(prompt)
    print (recipes)




user_input1=input(" enter you name")

print(" welcome to daniyal's recipe generator,", user_input1)

print("lets begin helping you cook today") 
print(" i will need 5 ingredients to help you get cooking unless you're lazy")

user_ingredient1=input(" enter your first ingredient")
user_ingredient2=input(" enter your second ingredient")
user_ingredient3=input(" enter your third ingredient")
user_ingredient4=input(" enter your fourth ingredient")
user_ingredient5=input(" enter your fifth ingredient")

recipe_generator(user_ingredient1,user_ingredient2,user_ingredient3, user_ingredient4, user_ingredient5)

