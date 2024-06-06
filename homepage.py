import streamlit as st

# Set the main title of the dashboard
st.title("EcoCAR Automation Showcase")

st.subheader("Background")
st.write(
    '''
    The UC Davis EcoCAR team needs to develop several dashboards (using 
    Streamlit and Python) to visualize their data. However, the 
    developers at EcoCAR have no automated methods to build, test, or 
    deploy these dashboards on EcoCAR’s new server.

    We have streamlined this process by creating a Jenkins CI/CD pipeline 
    that will automatically handle building, testing, and deployment of 
    dashboards from EcoCAR’s Bitbucket to EcoCAR’s new server.

    When developers open a Pull Request for a new/updated dashboard, a 
    new Jenkins build will occur. Jenkins will checkout the source code 
    from the Bitbucket repository. The pipeline uses Poetry to manage 
    and install any dependencies. The Black linter is used to scan for 
    code quality. If Poetry and Black run successfully, the pipeline 
    deploys the dashboard to either the production port or one of many 
    staging ports on the EcoCAR server.

    Besides streamlit, we also migrated some elements of EcoCAR’s old 
    server to its new server using Docker. Specifically, we deployed 
    dockerized instances of Airflow and PostgreSQL, with the former 
    being deployed via a separate Jenkins pipeline.
    '''
)

st.write("___")

st.subheader("Pipeline Architecture")
st.image("./EcoCAR Architecture Diagram.png")

st.write("___")

st.subheader("Streamlit Architecture")
st.image("./streamlitArchitecture.svg")

st.write("___")

st.subheader("Jenkins Demo")
st.video(data="./jenkins.mp4")
# st.video("./jenkins.mp4", format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

