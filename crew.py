from crewai import Crew,Process
from agents import planner, writer, editor
from task import plan, write, edit
import streamlit as st
from IPython.display import Markdown
crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=False
)
st.title("AI Multi-Agent System")

# Input for topic
topic = st.text_input("Enter the topic:", "Artificial Intelligence")

# Kick off the crew process
if st.button("Run Crew Process"):
    # Run the Crew process with user inputs
    result = crew.kickoff(inputs={"topic": topic})

    # Display the results
    st.markdown("### Process Results")
    st.markdown(result)
