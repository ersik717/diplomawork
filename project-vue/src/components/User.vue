<template>
	<div>
		<ul>
			<li v-for="user in users">
				<div>
				 {{ user.username }} and email is: {{ user.email }}
				 </div>
			</li>
		</ul>
	</div>
</template>

<script>
	import $ from 'jquery'
	import LoginTest from '@/components/Login'
	export default {
		name: "User",	

		data() {
			return {
				users: "",			
			}
		},
		created() {
			$.ajaxSetup({
				headers: {'Authorization': "JWT " + sessionStorage.getItem('access')},
			});
			this.loadUser()
		},
		methods: {
			loadUser() {
				$.ajax({
					url: "http://127.0.0.1:8000/api/users/",
					type: "GET",
					success: (response) => {
						this.users = response.results
						console.log(response)
						
					}

				})
			},
		}

	}

</script>