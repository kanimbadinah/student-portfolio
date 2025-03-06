import streamlit as st

#Set page title and icon

st.set_page_config(page_title="Student Portfolio",page_icon="🎓")

#Sidebar naviagtion

st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go To:",
	   ["Home","Projects","Skills","Settings","Contact"])
#Home section

if page =="Home":
	st.title("🎓 Student Portfolio")

	#Profile image
	uploaded_image = st.file_uploader("Uplaod Profile Picture", type=["jpg","png"])
	if uploaded_image is not None:
		st.image(uploaded_image, width=150, caption="Uploaded image")
	else:
		st.image("see.jpg", width=150, caption="Default image")
	#Student details (Editable!)
	name = st.text_input("Name: ", "Mahirwe Dinah")
	location = st.text_input("Location: ", "musanze,Rwanda")
	field_of_study = st.text_input("Field of Study: ",
	                               "Computer Science, SWE (year 3)")
	university = st.text_input("University: ", "INES - Ruhengeri")

	st.write(f"📍{location}")
	st.write(f"📚{field_of_study}")
	st.write(f"🎓{university}")

	# Resume download button
	with open("resume.pdf", "rb") as file:
		resume_bytes = file.read()
	st.download_button(label="📄Download Resume",
		data=resume_bytes,file_name="resume.pdf",
		mime="application/pdf")

	st.markdown("---")
	st.subheader("About Me")
	about_me = st.text_area("Short introduction about myself:",
		"I am a passionate AI look forward engineer!")
	st.write(about_me)

#Projects section
elif page =="Projects":
	st.title("💻 My Projects")

	with st.expander("🚦A Smart Traffic System"):
		st.write("Project Type: (Individual)")
		st.write(" Brief Description: (This system helps reduce traffic congestion, improve road safety, and enhance overall transportation efficiency)")

	with st.expander("🏡 Stock management"):
		st.write("Project Type: (Group work)")
		st.write("Description: (managing movement of products in stock by delete product, insert new product. and manage import and export reports) ")

	with st.expander("🏥 Booking patient appointment scheduling system"):
		st.write("Project Type: (Current Dissertation/Final Year Project )")
		st.write("Description: (The system aims to streamline appointment booking, reduce patient wait times, and improve overall hospital workflow. It will provide an intuitive interface for patients, doctors, and hospital administrators, enabling smooth scheduling, rescheduling, and cancellation of appointments.) ")

elif page =="Skills":
	st.title("🏹Skills and Achievements")

	st.subheader("Programming Languages ")
	skill_python = st.slider("Python",10,100,90)
	st.progress(skill_python)

	skill_js = st.slider("JavaScript",0,100,75)
	st.progress(skill_js)
	skill_SQL = st.slider("SQL",0,100,65)
	st.progress(skill_SQL)
	st.subheader("Machine Learning ")
	skill_DS = st.slider("Data Science ", 20, 100, 80)
	st.progress(skill_DS )
	st.subheader("Web Development")
	skill_HTML = st.slider("HTML", 20, 100, 80)
	st.progress(skill_HTML)
	skill_CSS = st.slider("CSS", 20, 100, 80)
	st.progress(skill_CSS)
	skill_React = st.slider("React", 20, 100, 80)
	st.progress(skill_React)
	skill_Flask = st.slider("Flask", 20, 100, 80)
	st.progress(skill_Flask)
	st.subheader("Cerfications & Achievements")
	st.write("✅ Completed Microsoft Office specialist in Powerpoint,word adn Excel ")
	st.write("✅ Certified of achievement for being third team in science club wed design competition @ Agahozo Shalom youth Village")

elif page == "Settings":
	st.title("🎨 Customize your profile")

	st.subheader("Upload a Profile Picture")
	uploaded_image = st.file_uploader("Choose a file", type=["jpg","png"])
	if uploaded_image:
		st.image(uploaded_image, width=150)

	st.subheader("✍ Edit Personal Info")

elif page =="Contact":
	st.title("🤳 Contact Me")

	with st.form("contact_form"):
		name = st.text_input("your name")
		email = st.text_input("Your Email")
		message=st.text_area("Your message 💌")

		submitted = st.form_submit_button("Send Message")
		if submitted:
			st.success("✅ Message sent successfully")

		st.write("📧 Email: kanimbadinah120@gmail.com")
		st.write("[🔗LinkedIn](https://www.linkedin.com/in/kanimba-dinah-843166337?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
		st.write("[📂GitHub](https://github.com/kanimbadinah)")

	st.sidebar.write("---")
	st.sidebar.write("🔹 Made with ❤ using My Watermelon")
