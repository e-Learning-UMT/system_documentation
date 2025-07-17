Title: Completion Webservices
Date: 2025-07-17
Slug: completion-webservices

# Platform Bayou UMT Web API – Course Completion Functions & Webhook Documentation

This document provides specific integration information for the following features of the `moodle_umt_web_api` plugin:

- `local_umt_web_api_get_course_completion_list` REST API function
- `local_umt_web_api_get_course_completion` REST API function
- Course completion webhook

---

## 1. `local_umt_web_api_get_course_completion_list`

### Purpose

Lists students with their course completion status. Supports optional filtering by completion state and time range.

### Endpoint

```
GET https://bayou.umt.edu.my/webservice/rest/server.php
```

### Required Parameters

- `wstoken`: Your Moodle REST API token
- `moodlewsrestformat`: Desired response format (typically `json`)
- `wsfunction`: `local_umt_web_api_get_course_completion_list`

### Optional Query Parameters

- `coursecode`: Course shortname/code
- `state`: Completion state (`completed`, `inprogress`, etc.)
- `timestart`: Start of time range (UNIX timestamp)
- `timeend`: End of time range (UNIX timestamp)

### Sample Request

```http
GET https://bayou.umt.edu.my/webservice/rest/server.php?wstoken=YOURTOKEN&moodlewsrestformat=json&wsfunction=local_umt_web_api_get_course_completion_list&coursecode=ABC123&state=completed&timestart=1704067200&timeend=1706755199
```

### Response

Returns a list of students, each with:
- `matricnumber`
- `fullname`
- `completionstate`
- `completiondate`
- etc.

---

## 2. `local_umt_web_api_get_course_completion`

### Purpose

Fetches course completion status for a specific student and/or course.

### Endpoint

```
GET https://bayou.umt.edu.my/webservice/rest/server.php
```

### Required Parameters

- `wstoken`: Your Moodle REST API token
- `moodlewsrestformat`: Desired response format (typically `json`)
- `wsfunction`: `local_umt_web_api_get_course_completion`

### Query Parameters

- `matricnumber` (optional): Student's matric number
- `coursecode` (optional): Course shortname/code

### Sample Request

```http
GET https://bayou.umt.edu.my/webservice/rest/server.php?wstoken=YOURTOKEN&moodlewsrestformat=json&wsfunction=local_umt_web_api_get_course_completion&matricnumber=MATRIC123&coursecode=ABC123
```

### Response

Returns status details for the specified student and/or course:
- `completionstate`
- `completiondate`
- Additional course/user data

---

## 3. Course Completion Webhook

### Purpose

Sends an HTTP POST notification to configured webhook URLs whenever a user completes a course.

### Configuration

- Set webhook URLs in plugin settings: **Completion webhook URLs** (`completionwebhook`)
- Multiple URLs supported (one per line)

### Trigger

- Fires on Moodle `core\event\course_completed` event

### Payload Format

Sent as JSON with content type `application/json`:

```json
{
  "coursecode": "ABC123",
  "studentmatric": "MATRIC123"
}
```

### Logging & Reports

- Every webhook call is logged (URL, payload, HTTP status, success)
- Logs are accessible and sortable in the plugin's report page

---

## References

- [Full Plugin Documentation](https://github.com/e-Learning-UMT/moodle_umt_web_api/WEB_API_DOCUMENTATION.md)
- [db/services.php](https://github.com/e-Learning-UMT/moodle_umt_web_api/blob/main/db/services.php)
- [README.md](https://github.com/e-Learning-UMT/moodle_umt_web_api/blob/main/README.md)
- [Webhook Observer](https://github.com/e-Learning-UMT/moodle_umt_web_api/blob/main/classes/observer.php)

---
